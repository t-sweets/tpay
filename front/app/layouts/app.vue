<template>
  <v-ons-navigator
    swipeable
    :page-stack="pageStack"
    @push-page="pushPage($event)"
    @pop-page="popPage($event)"
  ></v-ons-navigator>
</template>

<script>
import index from "~/pages/";

export default {
  // middleware: ["authenticated"],
  data() {
    return {
      pageStack: [index]
    };
  },
  methods: {
    pushPage(event) {
      console.log(this.pageStack);

      this.pageStack.push(event);
    },
    popPage(event) {
      if (event) this.pageStack.unshift(event);
      this.pageStack.splice(this.pageStack.length - 1, 1);
    }
  },
  mounted() {
    const html = document.documentElement;
    if (this.$ons.platform.isIPhoneX() && this.$route.query.standalone) {
      html.setAttribute("onsflag-iphonex-portrait", "");
    }
  }
};
</script>


<style lang="scss">
html {
  font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
  overflow: hidden;
  height: 100%;
}

html,
body {
  height: 100%;
  left: 0;
  overflow: hidden;
  position: fixed;
  top: 0;
  width: 100%;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}

ons-navigator {
  background-image: url("~assets/images/background.png");
  background-size: cover;
  background-repeat: no-repeat;
}

$blue-color: #04a3e4;
ons-page {
  text-align: center;

  // Color theme setting
  .page__background {
    // background-color: #fff;
    background-image: url("~assets/images/background.png");
    background-size: cover;
    background-color: transparent;
  }
  ons-toolbar {
    background-color: #fff !important;
  }
  .toolbar {
    .back-button,
    .toolbar-button,
    .toolbar__title {
      color: $blue-color;
    }
    .toolbar__title {
      font-weight: 600;
    }
    .back-button__icon {
      fill: $blue-color;
    }
  }

  ons-tab {
    .tabbar__button {
      color: #999;
    }
    :checked + .tabbar__button {
      color: $blue-color;
    }
  }
}
.tabbar {
  background-color: #fff !important;
  // background-color: transparent !important;
  // background-image: none;
  // backdrop-filter: blur(3px);
  // -webkit-backdrop-filter: blur(3px);
}

.el-message-box {
  width: 100% !important;
}
</style>

