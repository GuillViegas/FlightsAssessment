import { NgModule } from '@angular/core';
import { MatGridListModule, MatMenuModule, MatTabsModule, MatButtonModule, MatToolbarModule, MatCardModule,
	     MatTableModule, MatFormFieldModule, MatPaginatorModule, MatSortModule, MatInputModule,
		   MatSelectModule, MatDatepickerModule, MatNativeDateModule } from '@angular/material';

@NgModule({
  imports: [ MatGridListModule, MatMenuModule, MatTabsModule, MatButtonModule, MatToolbarModule, MatCardModule,
  MatTableModule, MatFormFieldModule, MatPaginatorModule, MatSortModule, MatInputModule,
  MatSelectModule, MatDatepickerModule, MatNativeDateModule ],

  exports: [ MatGridListModule, MatMenuModule, MatTabsModule, MatButtonModule, MatToolbarModule,
  MatCardModule, MatTableModule, MatFormFieldModule, MatPaginatorModule, MatSortModule, MatInputModule,
  MatSelectModule, MatDatepickerModule, MatNativeDateModule ]
})
export class AppMaterialModule { }
