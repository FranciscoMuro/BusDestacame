<template>
  <div class="wrapper">
    <div class="wrapperButton">
      <button type="button" class="buttonCrear" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="abrirModalParaCrear()">Agregar pasajero</button>
      <div class="tableWrapper">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Pasajero</th>
              <th scope="col">Numero de Autobus</th>
              <th scope="col">Opciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="pasajero in pasajeros" :key="pasajero.pasajeroId">
              <td>
                {{ pasajero.nombre }}
              </td>
              <td>
                {{ this.getAutbusInfoParaElPasajero(pasajero) }}
              </td>
              <td>
                <button type="button" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="abrirModalParaEditar(pasajero)">
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
                <button type="button" @click="eliminarClick(pasajero)">
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
                <span class="input-group-text">Nombre del pasajero</span>
                <input type="text" class="form-control" v-model="nombrePasajero" />
              </div>

              <div class="input-group mb-3">
                <span class="input-group-text">Autobuses</span>
                <select class="form-select" v-model="autobus">
                  <option v-for="autobus in autobuses" :key="autobus.busId">
                    {{ this.getAutbusInfoParaSeleccionarBus(autobus) }}
                  </option>
                </select>
              </div>
              <div class="buttonWrapperModal">
                <button type="button" @click="crearClick()" v-if="pasajeroId == 0" class="buttonCrearModal">Crear</button>
                <button type="button" @click="actualizarClick()" v-if="pasajeroId != 0" class="buttonCrearModal">Actualizar</button>
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
      pasajeros: [],
      trayectos: [],
      choferes: [],
      pasajeroId: 0,
      modalTitulo: '',
      nombrePasajero: '',
      autobus: '',
    };
  },
  methods: {
    obtenerDatos() {
      getApiAxios.get('pasajero/obtener/').then(response => {
        this.pasajeros = response.data;
      });
      getApiAxios.get('autobus/obtener/').then(response => {
        this.autobuses = response.data;
      });
      getApiAxios.get('trayecto/obtener/').then(response => {
        this.trayectos = response.data;
      });
      getApiAxios.get('chofer/obtener/').then(response => {
        this.choferes = response.data;
      });
    },
    abrirModalParaCrear() {
      this.modalTitulo = 'Agregar Pasajero';
      this.pasajeroId = 0;
      this.nombrePasajero = '';
      this.autobus = '';
    },
    abrirModalParaEditar(pasajero) {
      this.modalTitulo = 'Editar Pasajero';
      this.pasajeroId = pasajero.pasajeroId;
      this.nombrePasajero = pasajero.nombre;
      this.autobus = this.getAutbusInfoParaElPasajero(pasajero);
    },
    crearClick() {
      if (this.aunTieneAsientos()) {
        getApiAxios
          .post('/pasajero/crear/', {
            autobus: this.getBusId(),
            nombre: this.nombrePasajero,
          })
          .then(response => {
            this.obtenerDatos();
            alert(response.data);
          });
      } else {
        alert('El autobus seleccionado no cuenta con más lugares.');
      }
    },
    actualizarClick() {
      getApiAxios
        .put('/pasajero/actualizar/' + this.pasajeroId, {
          autobus: this.getBusId(),
          nombre: this.nombrePasajero,
        })
        .then(response => {
          this.obtenerDatos();
          alert(response.data);
        });
    },
    eliminarClick(pasajero) {
      if (!confirm('¿Seguro que desea eliminar al pasajero ' + pasajero.nombre + '?')) {
        return;
      }
      getApiAxios.delete('/pasajero/eliminar/' + pasajero.pasajeroId).then(response => {
        this.obtenerDatos();
        alert(response.data);
      });
    },
    getBusId() {
      const busId = this.autobus.split(' ')[3];
      return this.autobuses.find(autobus => busId == autobus.busId).busId;
    },
    getAutbusInfoParaElPasajero(pasajero) {
      const autobusInfo = this.autobuses.find(autobus => autobus.busId == pasajero.autobus);
      const trayectoInfo = this.trayectos.find(trayecto => autobusInfo.trayecto == trayecto.trayectoId);
      const choferInfo = this.choferes.find(chofer => chofer.choferId == autobusInfo.chofer);
      const informacionDelAutobus =
        'Numero de autobus: ' +
        autobusInfo.busId +
        ' Chofer: ' +
        choferInfo.nombre +
        ' Trayecto: ' +
        trayectoInfo.origen +
        '-' +
        trayectoInfo.destino +
        ' Fecha de salida: ' +
        autobusInfo.fecha_salida +
        ' Hora salida: ' +
        autobusInfo.hora_salida;
      return informacionDelAutobus;
    },
    getAutbusInfoParaSeleccionarBus(autobus) {
      const trayectoInfo = this.trayectos.find(trayecto => autobus.trayecto == trayecto.trayectoId);
      const choferInfo = this.choferes.find(chofer => chofer.choferId == autobus.chofer);
      const informacionDelAutobus =
        'Numero de autobus: ' +
        autobus.busId +
        ' Chofer: ' +
        choferInfo.nombre +
        ' Trayecto: ' +
        trayectoInfo.origen +
        '-' +
        trayectoInfo.destino +
        ' Fecha de salida: ' +
        autobus.fecha_salida +
        ' Hora salida: ' +
        autobus.hora_salida;
      return informacionDelAutobus;
    },
    aunTieneAsientos() {
      const asientosPorBus = this.pasajeros.filter(pasajero => pasajero.autobus == this.getBusId());
      return asientosPorBus.length + 1 <= 10;
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
  border: 1px solid #dfe1e6;
  box-shadow: 0px 1px 1px rgba(23, 43, 77, 0.25), 0px -3px 0px #03b3c4;
  border-radius: 3px;
}
.filtro {
  display: flex;
  align-items: baseline;
  margin: 10px;
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
.buttonCrear {
  display: flex;
  color: white;
  background-color: #03b3c4;
  border-radius: 3px;
  padding: 10px 10px 10px 10px;
  &:hover {
    background-color: #04c9db;
  }
}
</style>
