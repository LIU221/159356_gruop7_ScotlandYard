<template>
  <div class="choose">
    <el-container>
      <!-- <el-header>Choose Your Role</el-header> -->
      <el-main>
        <el-row>
          <el-col :span="12">
            <div>
              <el-container>
                <el-header>About Detective</el-header>
                <el-main>
                  <img
                    alt="detective"
                    width="500px"
                    height="500px"
                    src="../assets/detective.jpg"
                  />
                </el-main>
                <el-footer>
                  <el-radio v-model="radio" label="1" border>detective</el-radio>
                </el-footer>
              </el-container>
            </div>
          </el-col>
          <el-col :span="12">
            <div>
              <el-container>
                <el-header>About Mr.X</el-header>
                <el-main>
                  <img
                    alt="Mrx"
                    width="500px"
                    height="500px"
                    src="../assets/Mrx.jpg"
                  />
                </el-main>
                <el-footer>
                  <el-radio v-model="radio" label="2" border>Mr.X</el-radio>
                </el-footer>
              </el-container>
            </div>
          </el-col>
        </el-row>
      </el-main>
      <el-footer>
        <el-col :span="12" :offset="11">
          <el-button @click="toRolePage()" border>Confirm</el-button>
        </el-col>
      </el-footer>
    </el-container>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class Choose extends Vue {
  // @Prop() private msg!: string;
  private radio = "";
  public toRolePage() {
    if (this.radio == "1") {
      this.$router.push("./detective");
    } else {
      this.$router.push("./Mrx");
    }
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
