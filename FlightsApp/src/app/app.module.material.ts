import { NgModule } from '@angular/core';
import { MatGridListModule, MatMenuModule, MatTabsModule, MatButtonModule, MatToolbarModule, MatCardModule, 
	     MatTableModule, MatFormFieldModule, MatPaginatorModule, MatSortModule, MatInputModule } from '@angular/material';

@NgModule({
  imports: [ MatGridListModule, MatMenuModule, MatTabsModule, MatButtonModule, MatToolbarModule, MatCardModule, 
  MatTableModule, MatFormFieldModule, MatPaginatorModule, MatSortModule, MatInputModule ],

  exports: [ MatGridListModule, MatMenuModule, MatTabsModule, MatButtonModule, MatToolbarModule, 
  MatCardModule, MatTableModule, MatFormFieldModule, MatPaginatorModule, MatSortModule, MatInputModule ]
})
export class AppMaterialModule { }
