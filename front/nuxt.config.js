const pkg = require('./package')

module.exports = {
  mode: 'spa',
  srcDir: 'app',

  /*
  ** Headers of the page
  */
  head: {
    title: pkg.name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, viweport-fit=cover' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  router: {
    middleware: 'auth'
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [
    'element-ui/lib/theme-chalk/index.css'
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '~/plugins/element-ui',
    '~/plugins/my-functions',
    '~/plugins/vue-lazyload'
  ],

  /*
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/axios',
    ['@nuxtjs/dotenv',{ filename: '.env.production' }],
    '@nuxtjs/pwa',
    'nuxt-onsenui-module',
    'nuxt-fontawesome',
    '@nuxtjs/style-resources'
  ],

  styleResources: {
    scss: [
      '@/assets/sass/*/*/*'
    ]
  },

  fontawesome: {
    imports: [
      {
        set: '@fortawesome/free-solid-svg-icons',
        icons: ['fas']
      }
    ]
  },

  /*
  ** Build configuration
  */
  build: {
    transpile: [/^element-ui/],
    
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
      
    }
  },
  

  /*
   ** Generate configration 
   */
  generate: {
    routes: [
      '/login/',
      '/logout/',
      '/register/'
    ],
    subFolders: true
  },

  /*
   ** debug server configration
   */
  server: {
    port: 12000, // default: 3000
  },

  /*
   ** PWA manifest  
   */
  manifest: {
    name: "T-Pay",
    short_name: "T-Pay",
    lang: 'ja',
    display: "standalone",
  },
  meta: {
    mobileAppIOS: true,
    background_color: "#ffffff",
    viweport: 'width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, viewport-fit=cover',
    appleStatusBarStyle: "default"
  }
}