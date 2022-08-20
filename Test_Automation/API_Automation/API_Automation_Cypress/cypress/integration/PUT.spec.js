/// <reference types="cypress" />

let testData;

describe ('API Automation - PUT Method', () =>
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
    
    it('Test to verify that user is updated successfully with all the valid request data.', () => {
        cy.request({
            method : 'PUT',
            url : 'https://gorest.co.in/public/v2/users/10',
            headers : {
                'authorization' : 'Bearer ' + testData.accessToken
            },
            body : {
                "name" : "API Tester",
                "email" : email,
                "status" : "active"
            }
        })
            .should((Response) => {
            cy.log(JSON.stringify(Response.body))
            expect(Response.status).to.eq(200)
            expect(Response.body.id).is.exist
            expect(Response.body.name).to.eq('API Tester')
            expect(Response.body.email).to.eq(email)
            })
    })  

})

describe('API Automation - PUT Method with fixture' , () => 
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
    it('Test to verify that user is updated successfully with all the valid request data from fixtures file.', () => {
        cy.request({
            method : 'PUT',
            url : 'https://gorest.co.in/public/v2/users/10',
            headers : {
                'authorization' : 'Bearer ' + testData.accessToken
            },
            body : {
                "name" : testData.name,
                "email" : email,
                "status" : testData.status
            }
        })
            .should((Response) => {
            cy.log(JSON.stringify(Response.body))
            expect(Response.status).to.eq(200)
            expect(Response.body.id).is.exist
            expect(Response.body.name).to.eq('API Tester')
            expect(Response.body.email).to.eq(email)
            })
    })
})
