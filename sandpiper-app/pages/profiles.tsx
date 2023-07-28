import React from 'react'
import styled from 'styled-components';
import Breadcrumb from 'react-bootstrap/Breadcrumb';

import { StyledTable } from '../components/styledcomponents';
import { BodyContainer, BreadcrumbContainer } from '../components/containers';

const BreadcrumbProfiles= () => {
  return (
    <Breadcrumb>
      <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
      <Breadcrumb.Item active>Profiles</Breadcrumb.Item>
    </Breadcrumb>
  );
}

const WidgetsContainer = styled.div`
  padding: 1rem 0;
`


const Profiles = () => {
  return (
  <BodyContainer>
    <BreadcrumbContainer>
      <BreadcrumbProfiles/>
    </BreadcrumbContainer>
    
    <WidgetsContainer>
      Table widgets go here
    </WidgetsContainer>

      <StyledTable responsive striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            {Array.from({ length: 12 }).map((_, index) => (
              <th key={index}>Table heading</th>
            ))}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            {Array.from({ length: 12 }).map((_, index) => (
              <td key={index}>Table cell {index}</td>
            ))}
          </tr>
          <tr>
            <td>2</td>
            {Array.from({ length: 12 }).map((_, index) => (
              <td key={index}>Table cell {index}</td>
            ))}
          </tr>
          <tr>
            <td>3</td>
            {Array.from({ length: 12 }).map((_, index) => (
              <td key={index}>Table cell {index}</td>
            ))}
          </tr>
        </tbody>
      </StyledTable>
    
  </BodyContainer>
  )
}

export default Profiles
