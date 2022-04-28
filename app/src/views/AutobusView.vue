<template>
  <div class="wrapper">
    <div>
      <button type="button" class="buttonCrear" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="abrirModalParaCrear()">Agregar autobus</button>
      <div class="col-3 filtro">
        <input type="number" class="form-control inputFiltro" v-model="porcentajePasajerosFiltro" v-on:keyup.enter="FiltroPorPorcentaje()" placeholder="Filtro" />
        <button class="buttonFiltro" @click="FiltroPorPorcentaje()" v-if="busId == 0">Aceptar</button>
      </div>
      <div class="tableWrapper">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Numero de autobus</th>
              <th scope="col">Chofer</th>
              <th scope="col">Trayecto</th>
              <th scope="col">Fecha de salida</th>
              <th scope="col">Hora de salida</th>
              <th scope="col">Porcentaje de capacidad</th>
              <th scope="col">Opciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="bus in autobuses" :key="bus.id">
              <td>
                {{ bus.busId }}
              </td>
              <td>
                {{ this.choferes.find(chofer => chofer.choferId == bus.chofer).nombre }}
              </td>
              <td>
                {{ this.trayectos.find(trayecto => trayecto.trayectoId == bus.trayecto).origen }}
                -
                {{ this.trayectos.find(trayecto => trayecto.trayectoId == bus.trayecto).destino }}
              </td>
              <td>{{ bus.fecha_salida }}</td>
              <td>{{ bus.hora_salida }}</td>
              <td>{{ bus.procentajeDePasajeros }}%</td>
              <td>
                <button type="button" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="abrirModalParaEditar(bus)">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                    <path
                      d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
                    />
                    <path
                      fill-rule="evenodd"
                      d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
                    />
                  </svg>
                </button>
                <button type="button" @click="eliminarClick(bus)">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
                    <path
                      d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5ZM11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0H11Zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5h9.916Zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5Z"
                    />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- Comienza mdoal -->
      <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">
                {{ modalTitulo }}
              </h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">x</button>
            </div>

            <div class="modal-body">
              <div class="input-group mb-3">
                <span class="input-group-text">Choferes</span>
                <select class="form-select" v-model="Chofer">
                  <option v-for="chofer in choferes" :key="chofer.choferId">
                    {{ chofer.nombre }}
                  </option>
                </select>
              </div>

              <div class="input-group mb-3">
                <span class="input-group-text">Trayectos</span>
                <select class="form-select" v-model="Trayecto">
                  <option v-for="trayecto in trayectos" :key="trayecto.trayectoId">{{ trayecto.origen }}-{{ trayecto.destino }}</option>
                </select>
              </div>

              <div class="input-group mb-3">
                <span class="input-group-text">Fecha de salida</span>
                <input type="date" class="form-control" v-model="fecha_salida" />
              </div>

              <div class="input-group mb-3">
                <span class="input-group-text">Hora de salida</span>
                <input type="time" class="form-control" v-model="hora_salida" />
              </div>
              <div class="buttonWrapperModal">
                <button type="button" @click="crearClick()" v-if="busId == 0" class="buttonCrearModal">Crear</button>
                <button type="button" @click="actualizarClick()" v-if="busId != 0" class="buttonCrearModal">Actualizar</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getApiAxios } from '../services/Axios';

export default {
  name: 'Table',
  data() {
    return {
      autobuses: [],
      choferes: [],
      trayectos: [],
      pasajeros: [],
      autobusesSinFiltro: [],
      busId: 0,
      modalTitulo: '',
      fecha_salida: '',
      hora_salida: '',
      Chofer: '',
      Trayecto: '',
      porcentajePasajerosFiltro: '',
    };
  },
  methods: {
    obtenerDatos() {
      getApiAxios.get('autobus/obtener/').then(response => {
        this.autobuses = response.data;
        this.autobusesSinFiltro = response.data;
      });
      getApiAxios.get('chofer/obtener/').then(response => {
        this.choferes = response.data;
      });
      getApiAxios.get('trayecto/obtener/').then(response => {
        this.trayectos = response.data;
      });
      getApiAxios.get('pasajero/obtener/').then(response => {
        this.pasajeros = response.data;
      });
    },
    abrirModalParaCrear() {
      this.modalTitulo = 'Agregar autobus';
      this.busId = 0;
      this.fecha_salida = '';
      this.hora_salida = '';
      this.Chofer = '';
      this.Trayecto = '';
    },
    abrirModalParaEditar(bus) {
      this.modalTitulo = 'Editar autobus';
      this.busId = bus.busId;
      this.fecha_salida = bus.fecha_salida;
      this.hora_salida = bus.hora_salida;
      this.Chofer = this.choferes.find(chofer => chofer.choferId == bus.chofer).nombre;
      this.Trayecto = this.trayectos.find(trayecto => trayecto.trayectoId == bus.trayecto).origen + '-' + this.trayectos.find(trayecto => trayecto.trayectoId == bus.trayecto).destino;
    },
    crearClick() {
      getApiAxios
        .post('/autobus/crear/', {
          chofer: this.getChoferesId(),
          trayecto: this.getTrayectoId(),
          fecha_salida: this.fecha_salida,
          hora_salida: this.hora_salida,
        })
        .then(response => {
          this.obtenerDatos();
          alert(response.data);
        });
    },
    actualizarClick() {
      getApiAxios
        .put('/autobus/actualizar/' + this.busId, {
          chofer: this.getChoferesId(),
          trayecto: this.getTrayectoId(),
          fecha_salida: this.fecha_salida,
          hora_salida: this.hora_salida,
        })
        .then(response => {
          this.obtenerDatos();
          alert(response.data);
        });
    },
    eliminarClick(bus) {
      if (!confirm('¿Seguro que desea eliminar al chofer?')) {
        return;
      }
      getApiAxios.delete('/autobus/eliminar/' + bus.busId).then(response => {
        this.obtenerDatos();
        alert(response.data);
      });
    },
    getTrayectoId() {
      return this.trayectos.find(trayecto => this.Trayecto == trayecto.origen + '-' + trayecto.destino).trayectoId;
    },
    getChoferesId() {
      return this.choferes.find(chofer => this.Chofer == chofer.nombre).choferId;
    },
    FiltroPorPorcentaje() {
      let porcentajePasajerosFiltro = this.porcentajePasajerosFiltro;
      this.autobuses = this.autobusesSinFiltro.filter(autobusSinFiltro => autobusSinFiltro.procentajeDePasajeros.toString().trim().includes(porcentajePasajerosFiltro.toString().trim()));
    },
  },
  mounted: function () {
    this.obtenerDatos();
  },
};
</script>

<style scoped lang="scss">
.wrapper {
  display: flex;
  justify-content: center;
}
.tableWrapper {
  padding: 20px;
  margin-top: 30px;
  border-radius: 3px;
  box-shadow: 0px 1px 1px rgba(23, 43, 77, 0.25), 0px -3px 0px #03b3c4;
  border: 1px solid #dfe1e6;
}
.filtro {
  display: flex;
  align-items: baseline;
  margin: 10px;
}
.buttonCrear {
  display: flex;
  border-radius: 3px;
  padding: 10px 10px 10px 10px;
  color: white;
  background-color: #03b3c4;
  &:hover {
    background-color: #04c9db;
  }
}
.buttonWrapperModal {
  display: flex;
  justify-content: center;
}
.buttonCrearModal {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 3px;
  padding: 10px 10px 10px 10px;
  width: 150px;
  height: 45px;
  color: white;
  background-color: #03b3c4;
  &:hover {
    background-color: #04c9db;
  }
}
.buttonFiltro {
  border-radius: 3px;
  margin-top: 30px;
  margin-left: 10px;
  padding: 6px;
  background-color: #03b3c4;
  color: white;

  &:hover {
    background-color: #04c9db;
  }
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
