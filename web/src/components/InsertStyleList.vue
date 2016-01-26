<template>
  <div class="insert-style">
    <div class="insert-style_top"></div>
    <div class="insert-style_list">
      <ul class="insert-style_list_box"></ul>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Hello World!'
    }
  }
}
</script>

<style lang="sass">
.insert-style {
  widht: 100%;
}
.insert-style_top {
  background-color: rgba(245,245,245,0.9);
  height: 90px;
  text-align: center;
}
.insert-style_list {
  height: 569px;
  overflow-y: auto;
  overflow-x: hidden;
}
.insert-style_list_box {
  height: 5000px;

  margin-top: 0;
  margin-bottom: 11px;
  padding-left: 0;
}
</style>
