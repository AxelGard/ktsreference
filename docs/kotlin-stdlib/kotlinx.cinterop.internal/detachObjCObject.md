

# detachObjCObject

Detaches the Objective-C object from this Kotlin wrapper. More specifically, releases the Obj-C reference and zeroes the field where it is stored.

```kotlin
external fun detachObjCObject(obj: ObjCObject)(source)
```

```kotlin
import kotlinx.cinterop.ObjCObject
import kotlinx.cinterop.internal.detachObjCObject
import platform.Foundation.NSString

fun main() {
    // Create an Objective‑C NSString instance
    val nsString: NSString = NSString.stringWithString("Hello, ObjC!")

    // The NSString is also an ObjCObject
    val objcRef: ObjCObject = nsString

    // Detach the Obj‑C reference from the Kotlin wrapper
    detachObjCObject(objcRef)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop.internal/detach-obj-c-object.html)

    