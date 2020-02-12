<template>
    <div>
        <b-alert variant="success" show>{{ childMessage }}</b-alert>
    </div>
</template>

<script>
export default {
    props: ['childMessage']
}
</script>