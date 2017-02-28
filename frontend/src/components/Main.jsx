import React from 'react';
import { connect } from 'react-redux'
import HeaderContainer from '../containers/HeaderContainer';
import MenuContainer from '../containers/MenuContainer';


export default class Main extends React.Component {
  render() {
    return (
      <div
        style={{
          backgroundImage: `url(/static/images/background-space.png)`,
          backgroundSize: '500px auto',
          backgroundColor: '#111122',
        }}
      >
        <HeaderContainer />
        <MenuContainer />
        { this.props.children }
      </div>
    )
  }
}
