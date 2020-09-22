<template>
  <div class="detective">
    <el-row>
      <el-col :span="18" class="left">
        <LondonMap :mrx=-1 :detective=this.currentLocation :key="this.currentLocation"></LondonMap>
      </el-col>
      <el-col :span="6">
        <el-row>
          <img alt="detective" width="300px" height="300px" src="../assets/detective.jpg" />
        </el-row>
        <el-row>Current Round: {{ this.currentRound }}</el-row>
        <el-row>Current Role: You</el-row>
        <el-row>Ticket Mr.X used:</el-row>
        <el-row>Where will we go?</el-row>
        <el-row>
          <el-select v-model="vehicle" placeholder="Plz choose" @change=selectit(vehicle)>
            <el-option
              v-for="item in this.vehicles"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-row>
        <el-row>
          <el-radio v-model="value"
              v-for="item in this.endLocation"
              :key="item"
              :label="item"
              
            ></el-radio>
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
export default class Detective extends Vue {
  public currentRound: number = 1;
  public currentLocation: number = 1;
  public mrxLocation: number = 86;
  private vehicle = "";
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

  public open() {
    this.$alert("You Find Mr.X!", "You Win", {
      confirmButtonText: "End",
      callback: (action) => {
        this.$router.push("./choose");
      },
    });
  }

  public move() {
    console.log("move");
    if (this.value != 0) {
      this.currentLocation = this.value;
      console.log(this.currentLocation);
      this.currentRound += 1;
      this.update();
      if (this.currentLocation == this.mrxLocation) {
        this.open();
      }
    }
  }

  private update() {
    this.vehicle = "";
    this.value = 0;
    this.endLocation = [];
  }

  public selectit(vehicle: any) {
    if (vehicle == 'taxi') {
      this.endLocation = this.game.getNodeWithIndex(this.currentLocation).taxiDestination;
    }
    else if (vehicle == 'bus') {
      this.endLocation = this.game.getNodeWithIndex(this.currentLocation).busDestination;
    }
    else if (vehicle == 'undergroud') {
      this.endLocation = this.game.getNodeWithIndex(this.currentLocation).undergroundDestination;
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
</style>
