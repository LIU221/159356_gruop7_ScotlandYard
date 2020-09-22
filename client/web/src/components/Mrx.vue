<template>
  <div class="Mrx">
    <el-row>
      <el-col :span="18" class="left">
        <LondonMap :mrx="this.currentLocation" :detective="104" :key="this.currentLocation"></LondonMap>
      </el-col>
      <el-col :span="6">
        <el-row>
          <img alt="Mrx" width="300px" height="300px" src="../assets/Mrx.jpg" />
        </el-row>
        <el-row>Current Round: {{ this.currentRound }}</el-row>
        <el-row>Current Role: You</el-row>

        <el-row>
          Use 2x ticket
          <el-switch v-model="doubleFlag" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
        </el-row>
        <el-row>Where will we go?</el-row>
        <el-row>
          <el-select v-model="vehicle" placeholder="Plz choose" @change="selectit(vehicle)">
            <el-option
              v-for="item in this.vehicles"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-row>
        <el-row>
          <el-radio v-model="value" v-for="item in this.endLocation" :key="item" :label="item"></el-radio>
        </el-row>
        <el-row>
          <el-button type="primary" @click="move()">Move</el-button>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import LondonMap from "./LondonMap.vue";
import { Render } from "../game/render/Render";
import { Game } from "../game/Game";

@Component({
  components: {
    LondonMap,
  },
})
export default class Mrx extends Vue {
  public currentRound: number = 1;
  public currentLocation: number = 1;
  public detectiveLocations: number[] = [104];
  private vehicle = "";
  private doubleFlag = false;
  private value = 0;
  private endLocation = [];
  private game: Game = null;
  private vehicles = [
    {
      value: "taxi",
      label: "Taxi",
    },
    {
      value: "bus",
      label: "Bus",
    },
    {
      value: "undergroud",
      label: "Undergroud",
    },
  ];
  public created(): void {
    const game = new Game();
    this.game = game;
    this.currentLocation = game.getStartLocation();
  }

  public move() {
    console.log("move");
    if (this.value != 0) {
      this.currentLocation = this.value;
      console.log(this.currentLocation);
      if (!this.doubleFlag) {
        this.currentRound += 1;
      }
      this.update();
      if (this.currentLocation == this.detectiveLocations[0]) {
        this.open();
      }
    }
  }

  public open() {
    this.$alert("Detective Find You!", "You Lose", {
      confirmButtonText: "End",
      callback: (action) => {
        // this.$message({
        //   type: 'info',
        //   message: `action: ${ action }`
        // });
        this.$router.push("./choose");
      },
    });
  }

  private update() {
    this.vehicle = "";
    this.value = 0;
    this.doubleFlag = false;
    this.endLocation = [];
  }

  public selectit(vehicle: any) {
    if (vehicle == "taxi") {
      this.endLocation = this.game.getNodeWithIndex(
        this.currentLocation
      ).taxiDestination;
    } else if (vehicle == "bus") {
      console.log(this.endLocation);
      this.endLocation = this.game.getNodeWithIndex(
        this.currentLocation
      ).busDestination;
      console.log(this.endLocation);
    } else if (vehicle == "undergroud") {
      this.endLocation = this.game.getNodeWithIndex(
        this.currentLocation
      ).undergroundDestination;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.Mrx {
  font-family: Maragsa;
}
.el-row {
  font-family: Maragsa;
  padding: 8px;

  font-size: 28px;
}

@font-face {
  font-family: Maragsa;
  src: url("../assets/font/Maragsa.otf");
}
/* .left {
  background: pink;
} */
</style>
