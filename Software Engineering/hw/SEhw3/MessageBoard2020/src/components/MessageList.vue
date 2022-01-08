<template>
  <div id="message-list">
    <!--请修改这两行注释中间的代码，达到用多个MessageBlock来展示messageList数据的效果-->
    <!-- make list of messageblocks -->
    <li v-for="item in messageList" :key="item.id">
      <MessageBlock :title="item.title"
                  :content="item.content"
                  :user="item.user"
                  :timestamp = "item.timestamp"
                  :id="item.id"
                  />
    </li>
        <!--请修改这两行注释中间的代码，达到用多个MessageBlock来展示messageList数据的效果-->
  </div>
</template>

<script>
import MessageBlock from "@/components/MessageBlock"
//let counter = 1
// import uniqueId from 'lodash.uniqueid';


export default {
  name: "MessageList",
  components: {
    MessageBlock
  },
  props: {
    messageList: {
      type: Array,
      default: () => new Array(5).fill({
        id: this,
        title: "Hello",
        content: "Hello World!",
        user: "unknown",
        timestamp: new Date().getTime()
      })
    }
  },
  computed: {
    
  }
}
</script>

<style scoped>


li {
  list-style: none
}
</style>