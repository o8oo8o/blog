<template>
  <div class="content-header">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <div class="text-center">
            <div id="banner_id">
              <div v-html="this.$store.state.home_data.setting.banner"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// 广告功能
export default {
  name: "ContentHeader"
};
</script>

