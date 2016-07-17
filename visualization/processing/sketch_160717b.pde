PImage mapImage;
Table locationTable;
int rowCount;

Table dataTable;
float dataMinValue = MAX_FLOAT;
float dataMaxValue = MIN_FLOAT;

void setup() {
  size(640, 400);
  mapImage = loadImage("map.png");
  locationTable = new Table("locations.tsv");
  rowCount = locationTable.getRowCount();
  
  // Read the data table
  dataTable = new Table("random.tsv");

  // Find the minimum and maximum values
  for (int row = 0; row < rowCount; row++) {
    float value = dataTable.getFloat(row, 1);
    float score = dataTable.getFloat(row, 2);
    if (value > dataMaxValue) {
      dataMaxValue = value;
    }
    if (value < dataMinValue) {
      dataMinValue = value;
    }
  }
}


void draw() {
  background(255);
  image(mapImage, 0, 0);
  
  smooth();
  fill(192, 0, 0);
  noStroke();
  
  for (int row = 0; row < rowCount; row++) {
    String abbrev = dataTable.getRowName(row);
    float x = locationTable.getFloat(abbrev, 1);
    float y = locationTable.getFloat(abbrev, 2);
    drawData(x, y, abbrev);
  }
}


// Map the size of the ellipse to the data value
void drawData(float x, float y, String abbrev) {
  // Get data value for state
  float value = dataTable.getFloat(abbrev, 1);
  float score = dataTable.getFloat(abbrev, 2);
  
  // Re-map the value to a number between 2 and 40
  float mapped = map(value, dataMinValue, dataMaxValue, 9, 40);
  
  float percent = norm(score, -1, 1);
  color between = lerpColor(#FF0000, #00FF00, percent);  // red to blue
  fill(between);
  
  // Draw an ellipse for this item
  ellipse(x, y, mapped, mapped);
}
