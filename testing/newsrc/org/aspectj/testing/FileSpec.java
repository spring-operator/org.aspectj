/*******************************************************************************
 * Copyright (c) 2010 Contributors 
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-v10.html
 *
 * Contributors:
 *    Andy Clement - SpringSource
 *******************************************************************************/
package org.aspectj.testing;

import java.io.File;

import org.aspectj.tools.ajc.AjcTestCase;

/**
 * Support simple file system operations in a test spec. Example:<br>
 * &lt;file deletefile="foo.jar"/&gt; will delete the file foo.jar from the sandbox.
 * 
 * @author Andy Clement
 */
public class FileSpec implements ITestStep {

	private String toDelete;

	// private String dir;
	// private AjcTest test;

	public FileSpec() {
	}

	public void setDeletefile(String file) {
		this.toDelete = file;
	}

	public void addExpectedMessage(ExpectedMessageSpec message) {
	}

	public void execute(AjcTestCase inTestCase) {
		File sandbox = inTestCase.getSandboxDirectory();
		if (toDelete != null) {
			File targetForDeletion = new File(sandbox, toDelete);
			if (targetForDeletion.isFile()) {
				targetForDeletion.delete();
			} else {
				recursiveDelete(targetForDeletion);
			}
		}
	}

	private void recursiveDelete(File toDelete) {
		if (toDelete.isDirectory()) {
			File[] files = toDelete.listFiles();
			for (File f: files) {
				recursiveDelete(f);
			}
		}
		toDelete.delete();
	}

	public void setBaseDir(String dir) {
		// this.dir = dir;
	}

	public void setTest(AjcTest test) {
		// this.test = test;
	}

}
