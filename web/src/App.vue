<template>
  <div id="app">
    <!-- <img class="logo" src="./assets/logo.png"> -->
    <!-- <hello></hello> -->
    <div class="l-r-l">
      <div class="l-box">
        <insert-style-list></insert-style-list>
      </div>
      <div class="r-box">右</div>
    </div>
  </div>
</template>

<script>
import Hello from './components/Hello'
import InsertStyleList from './components/InsertStyleList'

export default {
  components: {
    Hello,
    InsertStyleList
  }
}
</script>

<style lang="sass">
@import "./assets/layout";

// 滚动条
::-webkit-scrollbar {   width: 10px;}
::-webkit-scrollbar-thumb {-webkit-box-shadow: inset 0 0 16px #645654; /*rgba(60,60,60,0.5)*/}
::-webkit-input-placeholder { /* WebKit browsers */   color:    #ddd;}
:-moz-placeholder { /* Mozilla Firefox 4 to 18 */color:    #ddd;}
::-moz-placeholder { /* Mozilla Firefox 19+ */ color:    #ddd;}
:-ms-input-placeholder { /* Internet Explorer 10+ */  color:    #ddd;}

// ::-webkit-scrollbar-track-piece{
//   background-color:#fff;
//   -webkit-border-radius:0;
// }
// ::-webkit-scrollbar{
//   width:8px;
//   height:8px;
// }
// ::-webkit-scrollbar-thumb{
//   height:50px;
//   background-color:#999;
//   -webkit-border-radius:4px;
//   outline:2px solid #fff;
//   outline-offset:-2px;
//   border: 2px solid #fff;
// }
// ::-webkit-scrollbar-thumb:hover{
//   height:50px;
//   background-color:#9f9f9f;
//   -webkit-border-radius:4px;
// }

body {
  font-family: Helvetica, sans-serif;
  background-color: #C9B3A5;
}

.l-box {
  width: 364px;
  height: 659px;
  overflow-y: auto;
  overflow-x: hidden;
  background: rgba(255,255,255,1);
}
.r-box {
  width: 390px;
  height: 500px;
  margin-left: 5px;
  background: rgba(255,255,255,1);
}
</style>
