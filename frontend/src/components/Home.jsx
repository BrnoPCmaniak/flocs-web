import React from 'react';
import { Link } from 'react-router'
import muiThemeable from 'material-ui/styles/muiThemeable';
import FloatingActionButton from 'material-ui/FloatingActionButton';
import ArrowDown from 'material-ui/svg-icons/hardware/keyboard-arrow-down';
import Scroll from 'react-scroll';
import SpaceGameContainer from '../containers/SpaceGameContainer';
import TaskEnvironmentContainer from '../containers/TaskEnvironmentContainer';
import NextTaskButtonContainer from '../containers/NextTaskButtonContainer';
import neuronsBackgroundPath from 'images/neurons-tile.png';


@muiThemeable()
export default class Home extends React.Component {
  render() {
    return (
      <div style={longPageStyle}>
        <section style={{ ...slideStyle, height: '85vh', backgroundColor: this.props.muiTheme.palette.canvasColor, color: '#fff' }} >
          <div style={slideContentStyle}>
            <h2>Prozkoumej tajemný vesmír</h2>
            <h2>a posbírej všechny diamanty</h2>
            <div>
              <SpaceGameContainer
                taskEnvironmentId="home-commands"
                controls={['fly', 'left', 'right', 'reset']}
              />
            </div>
            <div style={{ minHeight: 90, paddingTop: 25 }}>
            { this.props.spaceWorldDemoSolved &&
              <Scroll.Link to="intro-slide-2" smooth={true} duration={500}>
                <FloatingActionButton secondary={true}>
                  <ArrowDown />
                </FloatingActionButton>
              </Scroll.Link>
            }
            </div>
          </div>
        </section>

        <Scroll.Element name="intro-slide-2">
          <section style={{...slideStyle, backgroundColor: this.props.muiTheme.palette.primary1Color }} >
            <div style={slideContentStyle}>
              <h2>Nauč se ovládat vesmírnou loď</h2>
              <h2>pomocí počítačových programů</h2>
              <div
                style={{
                  position: 'relative',
                  height: 350,
                  width: 800,
                  margin: '0 auto',
                  border: '2px solid #777'
                }}
              >
                <TaskEnvironmentContainer taskEnvironmentId="home-program" />
              </div>
            </div>
          </section>
        </Scroll.Element>

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
