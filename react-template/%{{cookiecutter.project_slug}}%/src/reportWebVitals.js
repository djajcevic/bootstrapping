import {ConsoleInstrumentation, getWebInstrumentations, initializeFaro} from '@grafana/faro-web-sdk';
import { TracingInstrumentation } from '@grafana/faro-web-tracing';

const reportWebVitals = onPerfEntry => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

var _faro = null;
export function initFaroOTEL() {
  _faro = initializeFaro({
    url: `http://${process.env.REACT_APP_FARO_URL}`,
    apiKey: `${process.env.REACT_APP_FARO_APIKEY}`,
    trackWebVitalsAttribution: true,
    instrumentations: [...getWebInstrumentations(), new TracingInstrumentation(), new ConsoleInstrumentation()],
    app: {
      name: `%{{cookiecutter.project_slug}}%`,
      version: '1.0.0',
    },
  });
}

export const faro = _faro;

export default reportWebVitals;

