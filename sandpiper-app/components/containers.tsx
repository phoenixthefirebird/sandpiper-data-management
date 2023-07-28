import styled from 'styled-components';
import { colors } from '../styles/colors';

export const BodyContainer = styled.div`
  padding: 10px 20px;
  height: 100vh;
`

export const BreadcrumbContainer = styled.div`
  & nav > ol > .breadcrumb-item.active {
    color: ${colors.lightGrey};
  }

  & nav > ol > .breadcrumb-item.active::before {
    color: ${colors.lightGrey};
  }

  & nav > ol > li > a {
    color: ${colors.baseColor};
  }
`
