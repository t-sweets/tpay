<template>
  <v-ons-page>
    <v-ons-toolbar>
      <div class="left">
        <v-ons-back-button></v-ons-back-button>
      </div>
      <div class="center">カード登録</div>
    </v-ons-toolbar>
    <div class="qrReader" v-if="!isNoStreamApiSupport">
      <qrcode-reader :paused="paused" @init="onInit" @decode="onDecode"></qrcode-reader>
    </div>
    <div class="qrReader" v-else>
      <label class="qrcode-input" for="start-camera">
        <i class="el-icon-menu"></i>
        <span>カメラを起動する</span>
        <qrcode-capture id="start-camera" @decode="onDecode"/>
      </label>
    </div>
  </v-ons-page>
</template>

<script>
import { QrcodeCapture } from "vue-qrcode-reader";
import { mapMutations } from "vuex";
import registerIdmPage from "@/components/app/pages/registerIdmPage";
export default {
  data() {
    return {
      paused: false,
      isNoStreamApiSupport: false
    };
  },
  methods: {
    async onInit(promise) {
      try {
        await promise;
        // successfully initialized
      } catch (error) {
        if (error.name === "StreamApiNotSupportedError") {
          this.isNoStreamApiSupport = true;
        } else if (error.name === "NotAllowedError") {
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
    async onDecode(content) {
      this.paused = true;
      if (
        content.match(/tpay-stg\.t-lab\.cs\.teu\.ac\.jp/) &&
        content.match(/\?/) &&
        content.match(/method/)
      ) {
        const param = this.decodeParam(content);
        if (param.method == "register") {
          this.setIdm(param.idm);
          this.$emit("push-page", registerIdmPage);
        }
      } else {
        alert(content);
      }
    },
    decodeParam(string) {
      let params = {};
      const _params = string.split("?")[1].split("&");
      _params.forEach(param => {
        const s = param.split("=");
        params[s[0]] = s[1];
      });
      return params;
    },
    ...mapMutations("app/register-idm", ["setIdm"])
  },
  components: {
    QrcodeCapture
  }
};
</script>

<style lang="scss" scoped>
.qrcode-input {
  display: inline-block;
  cursor: pointer;
  color: #fff;
  background-color: #409eff;
  border-color: #409eff;
  border-radius: 5px;
  margin: 30px auto;
  padding: 10px;

  &:hover {
    background: #66b1ff;
    border-color: #66b1ff;
    color: #fff;
  }
  &:active {
    background: #3a8ee6;
    border-color: #3a8ee6;
    color: #fff;
  }

  input[type="file"] {
    display: none;
  }
}
</style>
