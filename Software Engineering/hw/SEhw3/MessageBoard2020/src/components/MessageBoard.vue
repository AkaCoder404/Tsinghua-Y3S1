<template>
    <div id="message-board">
        <el-container style="height:100%; border: 1px solid #eee">
            <el-header style="text-align: right; font-size: 10px">
                <el-button style="display: inline-block;margin-right: 15px;" 
                            v-on:click="postDialog.dialogVisible=true;"
                            >
                    <i class="el-icon-edit">发表</i>                       
                </el-button>
                <!--请修改这两行注释中间的代码完成"刷新"功能-->
                <el-button style="display: inline-block;margin-right: 15px;"
                        v-on:click="refreshAlert(); get();">
                <!--请修改这两行注释中间的代码完成"刷新"功能-->
                    <i class="el-icon-refresh" style="object-fit: fill">刷新</i>
                </el-button>
            </el-header>

            <el-main>
              <!--请补全这两行注释中间的messagelist-->
              <MessageList :messageList="sortedMessageList" />
              <!--请补全这两行注释中间的messagelist-->
              <!-- {{ state.username }}
              {{ postDialog.form.title }} -->  
            </el-main>

            <el-footer>@CST2020SE</el-footer>
        </el-container>
        <!--请补全这两行注释中间的PostDialog-->
        <PostDialog
            :dialogVisible.sync="postDialog.dialogVisible"
            v-on:childToParentClose="onChildClickCloseDialog"
            v-on:childToParent="onChildClick"
            >
        </PostDialog>
        <!--请补全这两行注释中间的PostDialog-->
        <el-dialog
                style="text-align: center"
                :title="alertDialog.text"
                :visible.sync="alertDialog.dialogVisible"
                v-if="is_sent.length > 0"
                width="40%">
        </el-dialog>
    </div>
</template>

<script>
    import MessageList from "@/components/MessageList";
    import PostDialog from "@/components/PostDialog";
    //uniqueId
    import uniqueId from 'lodash.uniqueid';
    // axois
    import axios from "axios" 
    // api
    import API from "../utils/API";


    export default {
        name: "MessageBoard",
        components: {
            MessageList,
            PostDialog
        },
        // 请在下方设计自己的数据结构及函数来完成最终的留言板功能
        data(){
            return {
                postDialog:{
                  dialogVisible:false,
                  form:{
                      title:"",
                      content:""
                    }
                },
                alertDialog:{
                    "text":"",
                    dialogVisible:false
                },
                state:{
                    username:  "",
                    username_valid:false
                    
                },
                is_sent: [{is_sent_tab:"false"}],
                messageList: [],
            }
        },
        methods:{
            sendAlert: function() {
                alert("发表 button is pressed");
            },
            refreshAlert: function() {
                //alert("刷新 button is pressed");
            },
            emitEventChanged () {
                this.$emit('CustomEventInputChanged', "Hello");
            },
            // postDialog emit information to parent (message board)
            onChildClick(value1, value2, value3) {
                //this.postDialog.form.username = value;
                this.state.username = value1;
                this.postDialog.form.title = value2;
                this.postDialog.form.content = value3;
                this.post();
            },
            onChildClickCloseDialog(value1){
                this.postDialog.dialogVisible = value1;
                
            },
            post() {
                
                let temp = []
                let temptitle = this.postDialog.form.title;
                let tempcontent = this.postDialog.form.content;
           
                axios.post("api/message", {
                title: temptitle,
                content: tempcontent
                })
                .then( (response) =>  {       
                    this.alertDialog.dialogVisible=true;
                    this.alertDialog.text = "发送";
                    this.get();
                    temp.push({is_sent_tab:"true"});
                    console.log(response);        
                })
                .catch( (error) =>  {
                    this.alertDialog.dialogVisible=true;
                    this.alertDialog.text = "发送失败";
                    temp.push({is_sent_tab:"false"});
                    // unsuccessful
                    console.log(error);
                });
                this.is_sent = temp;
            },
            // get request
            get() {
                //use axios to make request get request
                console.log(API.GET_MESSAGE_LIST.path);
                let temp = []
                axios.get("api/message", { }) 
                    .then(function (response) {
                        var i; 
                        for (i = 0; i < response.data.data.length; i++) {
                            temp.push({id:uniqueId("message-"), 
                                title: response.data.data[i].title,
                                content: response.data.data[i].content,
                                user: response.data.data[i].user,
                                timestamp: response.data.data[i].timestamp
                                })
                        }
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                        alert(error);
                    });  
                this.messageList = temp;  
            }       
        },
        computed: {
            //sort by timestamp, new ones on bottom
            sortedMessageList : function() {
                function compare(a,b) {
                    if (a.timestamp < b.timestamp) 
                        return -1;
                    if (a.timestamp > b.timestamp)
                        return 1;
                    return 0;
                }
                return this.messageList.slice().sort(compare);
            }
        }
    }


</script>


<style scoped>
    #message-board{
        height: calc(100vh - 16px);
    }
    .message-tab{
        display: block;
        padding: 10px;
        text-align: left;
    }
    .el-header {
        background-color: #B3C0D1;
        color: #333;
        line-height: 60px;
    }
    .el-footer {
        background-color: #B3C0D1;
        color: #333;
        line-height: 60px;
    }
    .el-aside {
        color: #333;
    }
</style>
