import React from 'react';
import { connect } from 'react-redux'
import { Link } from 'react-router'
import muiThemeable from 'material-ui/styles/muiThemeable';
import { recommend, getTaskForEnv } from '../actions/practiceActions'
import NextTaskButtonContainer from '../containers/NextTaskButtonContainer';
import PracticeContainer from '../containers/PracticeContainer';
import neuronsBackgroundPath from 'images/neurons-tile.png';


@connect((store) => {
    return {
        recommended: store.practice.recommendation
    }
})
@muiThemeable()
export default class Home extends React.Component {

  componentDidMount() {
    this.props.dispatch(getTaskForEnv('home', 'turning-right'));
    this.props.dispatch(recommend());
  }

  render() {
      console.log('theme', this.props.muiTheme);
      if (this.props.recommended == undefined) {
          return null
      }
      return (
        <div style={longPageStyle}>
          <section style={{ ...slideStyle, height: '85vh', backgroundColor: this.props.muiTheme.palette.canvasColor, color: '#fff' }} >
            <div style={slideContentStyle}>
              <h2>Prozkoumej tajemný vesmír</h2>
              <h2>a posbírej všechny diamanty</h2>
              <p>TBA: demo vesmirneho sveta s tlacitky vlevo-dopredu-doprava</p>
            </div>
          </section>

          <section style={{...slideStyle, backgroundColor: this.props.muiTheme.palette.primary1Color }} >
            <div style={slideContentStyle}>
              <h2>Nauč se ovládat vesmírnou loď</h2>
              <h2>pomocí počítačových programů</h2>
              <PracticeContainer
                taskEnvironmentId="home"
                containerStyle={{ position: 'relative', height: 400, width: 900, margin: '0 auto', border: '2px solid #777' }}
                taskCompletionDialogPosition="hidden"
              />
            </div>
          </section>

          <section
            style={{
              ...slideStyle,
              backgroundImage: `url(${neuronsBackgroundPath})`,
            }}
          >
            <div style={slideContentStyle}>
              <h2>Hra je poháněna umělou inteligencí,</h2>
              <h2>díky které se hra přizpůsobuje tvým dovednostem</h2>
            </div>
          </section>

          <section style={{...slideStyle, backgroundColor: this.props.muiTheme.palette.primary1Color }} >
            <div style={slideContentStyle}>
              <h2>Aplikaci vyvíjí tým Adaptabilního učení</h2>
              <h2>na Fakultě informatiky Masarykovy Univerzity</h2>
            </div>
          </section>

          <section
            style={{
              ...slideStyle,
              backgroundImage: `url(/static/images/background-space.png)`,
              backgroundSize: '500px auto',
              backgroundColor: '#111122',
              color: '#fff',
            }}
          >
            <div style={slideContentStyle}>
              <h2>Vyleť do vesmíru!</h2>
              <NextTaskButtonContainer />
            </div>
          </section>
        </div>
      )
  }
}

const longPageStyle = {
  width: '100%',
  height: '100%',
  margin: 0,
};

const slideStyle = {
  width: '100%',
  padding: '0 7%',
  display: 'table',
  margin: 0,
  height: '100vh',
};

const slideContentStyle = {
  display: 'table-cell',
  verticalAlign: 'middle',
  maxWidth: 1000,
  margin: '20px auto',
  textAlign: 'center',
};
