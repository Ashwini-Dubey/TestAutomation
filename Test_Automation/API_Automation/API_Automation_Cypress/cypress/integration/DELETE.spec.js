/// <reference types="cypress" />
/*
let testData;

describe ('API Automation - DELETE Method', () =>
{
    
    before(() => {
        cy.fixture('user_testdata/user_testdata').then((data) =>
        {
            cy.log(data)
            testData = data
        })
    })

    it('Test to verify that user is deleted successfully with all the valid request data.', () => {
        cy.request({
            method : 'DELETE',
            url : 'https://gorest.co.in/public/v2/users/12',
            headers : {
                'authorization' : 'Bearer ' + testData.accessToken
            }
        })
            .should((Response) => {
            cy.log(JSON.stringify(Response.body))
            expect(Response.status).to.eq(204)
            })
    })  

})

*/