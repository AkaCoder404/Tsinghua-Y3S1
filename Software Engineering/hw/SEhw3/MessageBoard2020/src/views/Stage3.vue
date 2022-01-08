<template>
  <div id="stage3">
    <!--修改下方的MessageList和PostDialog-->
    <MessageList :messageList ="messageList"/>
    <PostDialog
        :dialogVisible.sync="dialogVisible"
        v-on:childToParent="onChildClick"
        v-on:childToParentClose="onChildClickCloseDialog"
      />
  </div>
</template>

<script>
import MessageList from "@/components/MessageList.vue"
import PostDialog from "@/components/PostDialog.vue"
import uniqueId from 'lodash.uniqueid';

export default {
  name: 'Stage3',
  components: {
    MessageList,
    PostDialog
  },
  // 请在下方设计自己的数据结构和响应函数
  data(){
    return {
      messageList: [],
      dialogVisible: true,
    }
  },
  methods: {
    // postDialog emit information to parent (message board)
    onChildClick(value1, value2, value3) {
      this.messageList.push({id:uniqueId('message-'), title: value2, content: value3, user:value1})
      console.log(this.messageList[0])
      console.log("message submitted" +
          "\ntitle: " + value2 +
          "\ncontent: " + value3 + 
          "\nusername:  " + value1);
      //alert("title has been changed");
    },
    // postDialog emit information to parent (stage 3)
    onChildClickCloseDialog(value1){
      this.dialogVisible = value1;
    },
    // add to message board
    addMessage() {
      console.log("message added");
    }
  }
}
</script>