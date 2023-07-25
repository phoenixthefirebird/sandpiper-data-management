import React from 'react'
import styled from 'styled-components';

import Breadcrumb from 'react-bootstrap/Breadcrumb';

import { BodyContainer, BreadcrumbContainer } from '../components/containers';


const BreadcrumbHome= () => {
  return (
    <Breadcrumb>
      <Breadcrumb.Item active>Home</Breadcrumb.Item>
    </Breadcrumb>
  );
}

const Home = () => {
  return (
    <BodyContainer>
      <BreadcrumbContainer>
        <BreadcrumbHome/>
      </BreadcrumbContainer>

      Home
    </BodyContainer>
  )
}

export default Home