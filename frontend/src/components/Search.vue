<template>
    <b-container>
        <div class="col">
                <h3>Подсчёт слов, содержащихся на странице в интернете</h3>

                <notification :childMessage="notificationMessage" v-if="enableNotification"></notification>
        <b-row>
            <b-col cols="12" md="8">
                <button type="button" class="btn btn-success btn-lg d-block"
                v-b-modal.job-modal>
                    Новый поиск</button>
            </b-col>
            <b-col cols="6" md="4">
            <div class="text-right">
                <div class="btn-group" role="group" style="display: block;">
                <b-button type="button" class="btn btn-primary btn-sm"
                v-b-popover.hover.top="'Обновляет все результаты'" title=""
                @click="onUpdate" >
                Обновить результаты</b-button>
                &nbsp;
                <b-button type="button" class="btn btn-danger btn-sm"
                v-b-popover.hover.bottom="'Удаляет все записи'" title=""
                @click="onDelete">Очистить таблицу</b-button>
                </div>
            </div>
            </b-col>
        </b-row>

                <table class="table table-dark table-stripped table-hover">
            <thead class="thead-light">
                <tr>
                <th>ID</th>
                <th>Создано</th>
                <th>Адрес</th>
                <th>Искомое слово</th>
                <th>Статус</th>
                <th>Результат</th>
                <th>Обновлено</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="job in jobs" :key="job.id">
                    <td>{{ job.uuid }}</td>
                    <td>{{ job.created }}</td>
                    <td>{{ job.url }}</td>
                    <td>{{ job.word }}</td>
                    <td>
                        <span v-if="job.status == 'PENDING'">В процессе</span>
                        <span v-else-if="job.status == 'SUCCESS'">Завершено</span>
                        <span v-else>{{ job.status }}</span>
                    </td>
                    <td>{{ job.result }}</td>
                    <td>{{ job.updated }}</td>
                </tr>
            </tbody>
            </table>

<b-modal ref="addJobModal"
         id="job-modal"
         title="Новый поиск"
         hide-footer>
  <b-form @submit="onSubmit" class="w-100">
  <b-form-group id="form-description-group"
                label="Введите данные:"
                label-for="form-description-input">
    <b-form-input id="form-url-input"
                  type="text"
                  v-model="addJobForm.url"
                  required
                  placeholder="Где ищем?">
    </b-form-input>
    <b-form-input id="form-word-input"
                  type="text"
                  v-model="addJobForm.word"
                  required
                  placeholder="Что ищем?">
    </b-form-input>
  </b-form-group>
  
    <b-button type="submit" variant="primary">Добавить</b-button>
  </b-form>
</b-modal>

        </div>
    </b-container>
</template>

<script>
import Notification from './Notification.vue'
import axios from 'axios';

const dataURL = '/api/';
const updateURL = '/api/update/';
const deleteURL = '/api/delete/';

export default {
  name: 'Search',
  data() {
    return {
      jobs: [],
      addJobForm: {
        url: '',
        word: '',
      },
      notificationMessage: '',
      enableNotification: false,
    };
  },
  methods: {
    getJobs() {
      axios.get(dataURL)
        .then((response) => {
          this.jobs = response.data.jobs;
        });
    },
    resetForm() {
      this.addJobForm.url = '';
      this.addJobForm.word = '';
    },
    onSubmit(event) {
        event.preventDefault();
        this.$refs.addJobModal.hide();
        const requestData = {
            url: this.addJobForm.url,
            search_word: this.addJobForm.word,
        };
        axios.post(dataURL, requestData)
          .then(() => {
              this.getJobs();
          })
        this.notificationMessage = `Ищем "${requestData.search_word}" в "${requestData.url}"`
        this.enableNotification = true
        this.resetForm()
    },
    onUpdate(event) {
        event.preventDefault();
        axios.get(updateURL)
          .then(() => {
              this.getJobs();
          })
        this.notificationMessage = 'Результаты обновлены'
        this.enableNotification = true
    },
    onDelete(event) {
        event.preventDefault();
        axios.get(deleteURL)
          .then(() => {
              this.getJobs();
          })
        this.notificationMessage = 'Результаты удалены'
    },
  },
  components: {
    notification: Notification
  },
  created() {
    this.getJobs();
  },
};
</script>
