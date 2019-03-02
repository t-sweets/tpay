<template>
  <div class="navbar">
    <div class="navbar-header">
      <a href class="navbar-brand">T-PAY</a>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.navbar {
  width: 90vw;
  display: inline-block;

  .navbar-header {
    position: relative;
    &::before,
    &::after {
      display: table;
      content: " ";
    }

    a {
      color: #fff;
      text-decoration: none;
      &.navbar-brand {
        @include pc {
          float: left;
        }
        @include sp {
          float: none;
        }
        padding: 14px 15px;
        font-size: 18px;
        line-height: 30px;
      }
    }
  }
}
</style>

