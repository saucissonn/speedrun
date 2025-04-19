/*
pyodide-mkdocs-theme
Copyleft GNU GPLv3 🄯 2024 Frédéric Zinelli

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.
If not, see <https://www.gnu.org/licenses/>.
*/


import { PyodideSectionsRunner, RunningProfile } from "2-pyodideSectionsRunner-runner-pyodide"


export class BtnRunner extends PyodideSectionsRunner {

  // @Override
  build(){
    super.build()

    this.runner = this.lockedRunnerWithBigFailWarningFactory(
      RunningProfile.PROFILE.btn,
      this.setupRuntimeBtn,
      ()=>null,                 // No "user" action!
      this.teardownRuntime,
    )

    $('#'+this.id).find("button").on('click', this.runner)
  }

  async setupRuntimeBtn(){
    // Can get an argument (eventOrCmd), depending on how it's run/called.
    //    => Override to not transmit it
    return await this.setupRuntime()
  }
}

CONFIG.CLASSES_POOL.PyBtn = BtnRunner
