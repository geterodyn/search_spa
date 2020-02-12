<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  data() {
    return {

    };
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
button, h3 {
  margin-top: 20px;
  margin-bottom: 20px;
}
td, th {
  border: 1px solid black;
}
h3 {
  background-color:cadetblue;
}
</style>
