<template>
  <div class="wrapper">
    <nav>
      <ul>
        <li class="li_home">
          <router-link class="button" to="/">Atobuses</router-link>
        </li>
        <li class="li_home">
          <router-link class="button" to="/pasajeros">Pasajeros</router-link>
        </li>
        <li class="li_home">
          <router-link class="button" to="/trayectos">Trayectos</router-link>
        </li>
        <li class="li_home">
          <router-link class="button" to="/choferes">Choferes</router-link>
        </li>
      </ul>
    </nav>
  </div>
  <router-view />
</template>

<style lang="scss">
.wrapper {
  display: flex;
  justify-content: center;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

li {
  margin: 10px;
}

nav {
  ul {
    display: flex;
    padding: 20px;
    margin-top: 30px;
    border: 1px solid #dfe1e6;
    box-shadow: 0px 1px 1px rgba(23, 43, 77, 0.25);
    border-radius: 3px;
  }
  .button {
    display: flex;
    color: white;
    background-color: #03b3c4;
    border-radius: 4px;
    padding: 10px 10px 10px 10px;
    &:hover {
      background-color: #04c9db;
    }
  }
}
</style>
