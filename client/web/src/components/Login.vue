<template>
  <div class="login">
    <el-row class="login-form">
      <el-col :span="6" :offset="9">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="Username" placeholder="Input your username">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="Password">
            <el-input placeholder="Input your password" v-model="form.password" show-password></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">Login</el-button>
            <el-button @click="toRegister">Register</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class Login extends Vue {
  private form = {
    name: "",
    password: "",
  };
  onSubmit() {
    // TODO: check from
    console.log(this.form);
    if (this.form.name == 'admin' && this.form.password == 'admin') {
       this.$message({
            message: "Success",
            type: "success",
          });
          this.$router.push("./choose");
    } else {
      this.$message.error("Error");
    }
    // this.axios
    //   .post("http://localhost:8000/users/login/", {
    //     name: this.form.name,
    //     password: this.form.password,
    //   })
    //   .then((response) => {
    //     if (response.data == 1) {
    //       this.$message({
    //         message: "Success",
    //         type: "success",
    //       });
    //       this.$router.push({
    //         name: "Main",
    //       });
    //     } else if (response.data == -1) {
    //       this.$message.error("Error");
    //     } else if (response.data == -2) {
    //       this.$message.error("Unknow Id");
    //     }
    //   });

  }
  toRegister() {
    this.$router.push({
      name: "Register",
    });
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
