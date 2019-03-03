import Cookie from "js-cookie";
export default async function ({ route, store, redirect }) {
  let auth = Cookie.get("auth");
  if (auth) await store.commit("setAuth", auth);
  if (!store.state.auth.Authorization && route.path!= "/login" && route.path != "/register" && route.path!= "/logout") {
    return redirect('/login')
  } else if (store.state.auth.Authorization && (route.path == "/login" || route.path == "/register" || route.path == "/logout")) {
    return redirect('/')
  }
}