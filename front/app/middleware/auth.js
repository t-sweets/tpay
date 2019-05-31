import Cookie from "js-cookie";
export default async function ({ route, store, redirect }) {
  // Cookie情報から認証情報を取得
  let auth = Cookie.get("auth");
  if (auth) await store.commit("setAuth", auth);

  // Register IDM
  if (route.query.method == "register" && route.query.idm) {
    await store.commit("app/register-idm/setIdm", route.query.idm)
  }

  /*
   ** Authentication 
   */
  if (!store.state.auth.Authorization && route.path != "/login/" && route.path != "/register/" && route.path!= "/logout/") {
    return redirect('/login/')
  } else if (store.state.auth.Authorization && (route.path == "/login/" || route.path == "/register/" || route.path == "/logout/")) {
    return redirect('/')
  }
}