import styled from 'styled-components';
import { colors } from '../styles/Colors';

export const BodyContainer = styled.div`
  padding: 10px 50px;
  height: 100vh;
`

export const BreadcrumbContainer = styled.div`
  border-radius: 3px;
  display: flex;
  align-items: center;
  padding-top: 1rem;
  padding-left: 0.5rem;
  background: ${colors.darkGrey};

  & nav > ol > .breadcrumb-item.active {
    color: ${colors.lightGrey};
  }

  & nav > ol > li > a {
    color: ${colors.accent};
  }
`