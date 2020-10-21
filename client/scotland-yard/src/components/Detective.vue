<template>
  <div class="detective">
    <el-row>
      <el-col :span="18" class="left">
        <LondonMap
          v-if="updateFlag"
          :mrx="this.showmrxLocation"
          :detectives="this.detectiveLocations"
          :key="this.currentLocation"
        ></LondonMap>
      </el-col>
      <el-col :span="6">
        <el-row>
          <img
            alt="detective"
            width="300px"
            height="300px"
            src="../assets/detective.jpg"
          />
        </el-row>
        <el-row id="23463">Current Round: {{ this.currentRound }}</el-row>
        <el-row>Current Role: You</el-row>
        <el-row>Ticket Mr.X used:</el-row>
        <el-row>Where will we go?</el-row>
        <el-row>
          <el-select
            v-model="vehicle"
            placeholder="Plz choose"
            @change="selectit(vehicle)"
          >
            <el-option
              v-for="item in this.vehicles"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-row>
        <el-row>
          <el-radio
            v-model="value"
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
import { Client } from "../game/net/client";
import WebSocket from "isomorphic-ws";

@Component({
  components: {
    LondonMap,
  },
})
export default class Detective extends Vue {
  public updateFlag: boolean = true;
  public currentRound: number = 1;
  public currentLocation: number = 1;
  public mrxLocation: number = -1;
  public showmrxLocation: number = -1;
  public detectiveLocations: number[] = [];
  public disabledFlag: boolean = true;
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
    // Client.gClient = new Client("ws://49.232.18.122:8021/ws/game");
    Client.gClient = new Client("ws://localhost:8020/ws/game");
    Client.gClient.ws.onopen = (evt: WebSocket.OpenEvent) => {
            Client.gClient.doSend({
        message: {
          round: this.currentRound,
          detective: this.currentLocation,
          mrx: -1,
          count: 0,
          detectives: []
        },
      });
        };
    Client.gClient.ws.onmessage = (evt: WebSocket.OpenEvent) => {
      console.log("WebSocket接收消息：");
      let data = JSON.parse(evt.data)["message"];
      const count = data["count"];
      if (data['round'] == -1) {
        this.open();
      }
      this.detectiveLocations = data['detectives']
      this.mrxLocation = data["mrx"];
      const revealRounds = [3, 8, 13, 18, 24];
      for (const iterator of revealRounds) {
        if (data["round"] == iterator) {
          this.showmrxLocation = data["mrx"];
        }
      }
      this.reloadMap();
    };
    this.currentLocation = game.getStartLocation();
  }

  public reloadMap() {
    this.updateFlag = false;
    this.$nextTick(() => {
      this.updateFlag = true;
    });
  }

  public open() {
     Client.gClient.doSend({
        message: {
          round: -1,
          detective: this.currentLocation,
          mrx: -1,
          count: 0,
          detectives: []
        },
      })
    this.$alert("You Find Mr.X!", "You Win", {
      confirmButtonText: "End",
      callback: (action) => {
        this.$router.push("./choose");
      },
    });
  }

  public move() {
    if (this.value != 0) {
      this.currentLocation = this.value;
      console.log(this.currentLocation);
      this.currentRound += 1;
      Client.gClient.doSend({
        message: {
          round: this.currentRound,
          detective: this.currentLocation,
          mrx: -1,
          count: 0,
          detectives: []
        },
      });
      if (this.currentLocation == this.mrxLocation) {
        this.open();
      }
      this.update();
      
    }
  }

  private update() {
    this.vehicle = "";
    this.value = 0;
    this.endLocation = [];
  }

  public selectit(vehicle: any) {
    if (vehicle == "taxi") {
      this.endLocation = this.game.getNodeWithIndex(
        this.currentLocation
      ).taxiDestination;
    } else if (vehicle == "bus") {
      this.endLocation = this.game.getNodeWithIndex(
        this.currentLocation
      ).busDestination;
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
</style>
