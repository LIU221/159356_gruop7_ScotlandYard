<template>
  <div class="LondonMap">
    
    <img
      id="detective"
      class="hidden-img"
      alt="board"
      width="30px"
      height="30px"
      src="../assets/detective.jpg"
    />
    <img id="mrx" class="hidden-img" alt="Mrx" width="30px" height="30px" src="../assets/Mrx.jpg" />
    <img
      id="board"
      class="hidden-img"
      alt="board"
      width="1000px"
      height="700px"
      src="../assets/board.jpg"
    />
    <div id="display-map"></div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { Render } from "../game/render/Render";
import { Game } from "../game/Game";

@Component
export default class LondonMap extends Vue {
  @Prop() private mrx: number;
  @Prop() private detective: number;
  public mounted(): void {
    const ele = document.getElementById("display-map") as HTMLElement;
    const board = document.getElementById("board") as HTMLImageElement;
    const mrxImg = document.getElementById("mrx") as HTMLImageElement;
    const detectiveImg = document.getElementById("detective") as HTMLImageElement;
    const render = new Render(ele, board.height, board.width);
    const game = new Game();
    const mrxNode = this.mrx;
    const detectiveNode = this.detective;
    console.log(mrxNode);
    board.onload = function () {
      render.drawMap(board);
      if (mrxNode != -1) {
        const gameNode = game.getNodeWithIndex((mrxNode));
        console.log(gameNode)
        render.drawPortrait(mrxImg, gameNode.x, gameNode.y, 30, 30);
      }
      if (detectiveNode != -1) {
        const gameNode = game.getNodeWithIndex((detectiveNode));
        console.log(gameNode)
        render.drawPortrait(detectiveImg, gameNode.x, gameNode.y, 30, 30);
      }
    };
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hidden-img {
  display: none;
}
</style>
