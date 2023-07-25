import React from 'react'
import styled from 'styled-components';

import Breadcrumb from 'react-bootstrap/Breadcrumb';

import { BodyContainer, BreadcrumbContainer } from '../components/containers';

const BreadcrumbProfiles= () => {
  return (
    <Breadcrumb>
      <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
      <Breadcrumb.Item active>Profiles</Breadcrumb.Item>
    </Breadcrumb>
  );
}

const Profiles = () => {
  return (
  <BodyContainer>
    <BreadcrumbContainer>
      <BreadcrumbProfiles/>
    </BreadcrumbContainer>

    Profiles
  </BodyContainer>
  )
}

export default Profiles