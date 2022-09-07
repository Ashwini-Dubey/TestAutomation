/// <reference types="cypress" />

let testData;

describe('API Automation - POST Method with fixture' , () => 
{
    const uid = () => Cypress._.random(0,1e6)
    const id = uid()
    const email = `cyapitest${id}@yopmail.com`

    before(() => {
        cy.fixture('user_testdata/user_testdata').then((data) =>
        {
            cy.log(data)
            testData = data
        })
    })
    it('Test to verify that user is created successfully with all the valid request data from fixtures file.', () => {
        cy.request({
            method : 'POST',
            url : 'https://api.getsigneasy.com/v4/user/check',
            headers : {
                'content-type' : 'application/json'
            },
            body : {
                "email" : email
            }
        })
            .should((Response) => {
            cy.log(JSON.stringify(Response.body))
            expect(Response.status).to.eq(200)
            expect(Response.body.email).to.contain('no_account_exists')
                
        })
    })
})