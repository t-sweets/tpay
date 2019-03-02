<template>
  <section class="container">
    <div class="title">{{selectedSideMenu.title}}</div>
    <el-table :data="menusList" border>
      <el-table-column prop="id" label="no." width="80px"></el-table-column>
      <el-table-column prop="title" label="title">
        <template slot-scope="scope">
          <el-button type="text">{{scope.row.title}}</el-button>
        </template>
      </el-table-column>
      <el-table-column prop="description" label="description"></el-table-column>
    </el-table>
  </section>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {};
  },
  methods: {
    open() {}
  },
  computed: {
    ...mapGetters("admin", ["menusList", "selectedSideMenu"])
  },
  layout: "admin"
};
</script>

<style lang="scss" scoped>
.container {
  .title {
    position: relative;
    color: white;
    padding: 0.5em 0.5em 0.5em 1.4em;
    background-color: #446689;
    border-radius: 5px;
    &::after {
      position: absolute;
      top: 50%;
      left: 0.7em;
      transform: translateY(-50%);
      content: "";
      width: 5px;
      height: 25px;
      background-color: white;
    }
  }
}
</style>

