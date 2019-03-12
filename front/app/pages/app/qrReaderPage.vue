<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="left">
        <v-ons-back-button></v-ons-back-button>
      </div>
      <div class="center">カード登録</div>
    </v-ons-toolbar>
    <div class="qrReader">
      <qrcode-reader :paused="paused" @init="onInit" @decode="onDecode"></qrcode-reader>
    </div>
  </v-ons-page>
</template>

<script>
export default {
  data() {
    return {
      paused: false
    };
  },
  methods: {
    async onInit(promise) {
      try {
        await promise;
        // successfully initialized
      } catch (error) {
        if (error.name === "NotAllowedError") {
          // user denied camera access permisson
        } else if (error.name === "NotFoundError") {
          // no suitable camera device installed
        } else if (error.name === "NotSupportedError") {
          // page is not served over HTTPS (or localhost)
        } else if (error.name === "NotReadableError") {
          // maybe camera is already in use
        } else if (error.name === "OverconstrainedError") {
          // passed constraints don't match any camera. Did you requested the front camera although there is none?
        } else {
          // browser is probably lacking features (WebRTC, Canvas)
        }
      } finally {
        // hide loading indicator
      }
    },
    onDecode(content) {
      this.paused = true;
      if (
        content.match(/tpay-stg\.t-lab\.cs\.teu\.ac\.jp/) ||
        content.match(/localhost/)
      ) {
        location.href = content;
      } else {
        alert(content);
      }
    }
  }
};
</script>

<style lang="scss" scoped>
#video {
  width: 100%;
  height: 100%;
}
</style>
