library(shiny)
library(datasets)

# Define UI for application that draws a graphic
ui <- fluidPage(
   
  titlePanel("Design Pattern 9: Interactive Application in R (Shiny)"),

  # Sidebar with a select input for provinces
  sidebarLayout(
    sidebarPanel(
       selectInput("place", "Select one of 47 French-speaking provinces of Switzerland", 
                   as.factor(row.names(swiss)), selected = as.factor("Courtelary"))
    ),
    
    # Show a plot
    mainPanel(
       plotOutput("distPlot")
    )
  )
)

# Define how and what should it be created 
server <- function(input, output) {
   
  output$distPlot <- renderPlot({
    # format & prepare the "long" data 
    swiss_Religion <- as.data.frame(swiss[,5])
    colnames(swiss_Religion)[1] <- "Catholic"
    swiss_Religion$Place <- row.names(swiss)
    swiss_Religion$Protestant <- round(100-swiss_Religion$Catholic,2)
    swiss_Religion$LabelCatholic <- paste("Catholic\n ", swiss_Religion$Catholic, "%")
    swiss_Religion$LabelProtestant <- paste("Protestant\n ", swiss_Religion$Protestant, "%")
    
    exactPlace <- input$place
    pie(as.numeric(swiss_Religion[swiss_Religion$Place == exactPlace,c(1,3)]), 
        labels = c(swiss_Religion[swiss_Religion$Place == exactPlace,c(4,5)]), 
        main=paste0("Distribution of Religion in Percent at about 1888 in ", exactPlace, 
                    ", Switzerland.\n Source: Mosteller & Tukey (1977)"))
  })
}

shinyApp(ui = ui, server = server)

