<template>
  <div class="Register">
    <el-row>
      <el-col :span="6" :offset="9">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="UserName">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="Sex">
            <el-radio-group v-model="form.sex">
              <el-radio label="Man"></el-radio>
              <el-radio label="Woman"></el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="Phone">
            <el-input placeholder="please input your phone number" v-model="form.phone"></el-input>
          </el-form-item>
          <el-form-item label="Password">
            <el-input placeholder="Please input your password" v-model="form.password" show-password></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">Sign up</el-button>
            <el-button @click="toBack">Cancel</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class Register extends Vue {
  private form = {
        name: "",
        sex: "Man",
        phone: null,
        password: ""
      };
  onSubmit() {
      // TODO: 进行输入检查，判断输入的合法性
      console.log(this.form);

      this.axios
        .post("http://49.232.18.122:8020/users/register/", {
          userId: this.form.name,
          sex: this.form.sex,
          phone: this.form.phone,
          password: this.form.password
        })
        .then(response => {
          if (response.data == 1) {
            this.$message({
              message: "Success",
              type: "success"
            });
            this.$router.push("Login");
          } else if (response.data == -1) {
            this.$message.error("The Id is used by other");
          } else {
            this.$message.error("Unknow Error");
          }
        });
    }
  toBack() {
      this.$router.push("Login");
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.choose {
  background: url("../assets/London.jpg");
  background-size: 100% 100%;
  background-repeat: no-repeat;
}

.choose {
  font-family: Maragsa;
}
.el-row {
  font-family: Maragsa;
  padding: 8px;
  font-size: 28px;
}

.el-header {
  font-family: Maragsa;
  font-size: 34px;
}

.el-button {
  font-family: Maragsa;
  font-size: 34px;
}

@font-face {
  font-family: Maragsa;
  src: url("../assets/font/Maragsa.otf");
}
</style>
