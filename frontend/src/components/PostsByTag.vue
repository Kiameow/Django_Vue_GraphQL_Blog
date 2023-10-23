<template>
  <div>
    <h2>包含 #{{ $forceUpdate.params.tag }} 标签的帖子</h2>
    <PostList v-if="posts" :posts="posts" />
  </div>
</template>

<script>
import PostList from '@/components/PostList'

export default {
  name: 'PostsByTag',
  components: {
    PostList,
  },
  data () {
    return {
      posts: null,
    }
  },
}
</script>