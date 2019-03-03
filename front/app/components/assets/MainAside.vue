<template>
  <div class="aside-buttons">
    <el-table :data="sidemenus" border style="width: 100%">
      <el-table-column prop="date" label="Menus">
        <template slot-scope="scope">
          <el-button type="text" @click="setSideMenuIndex(scope.$index)">{{scope.row.title}}</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  data() {
    return {};
  },
  methods: {
    ...mapMutations("admin", ["setSideMenuIndex"])
  },
  computed: {
    ...mapState("admin", ["sidemenus"])
  }
};
</script>

<style lang="scss" scoped>
.aside-buttons {
  width: 100%;
  button {
    width: 100%;
  }
}
</style>

<style lang="scss">
.aside-buttons {
  .el-table th,
  .el-table td {
    padding: 0px;
  }
}
</style>
