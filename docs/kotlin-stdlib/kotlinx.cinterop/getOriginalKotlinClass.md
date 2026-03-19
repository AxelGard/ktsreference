

# getOriginalKotlinClass

If objCClass is a class generated to Objective-C header for Kotlin class, returns KClass for that original Kotlin class.

```kotlin
fun getOriginalKotlinClass(objCClass: ObjCClass): KClass<*>?(source)
```

```kotlin
import platform.objc.ObjCClass
import platform.objc.objc_getClass
import kotlinx.cinterop.getOriginalKotlinClass
import kotlin.reflect.KClass

// A plain Kotlin class
class MyKotlinClass

fun main() {
    // Obtain the Objective‑C class that the Kotlin/Native compiler generated
    val objcClass = objc_getClass("MyKotlinClass") as ObjCClass

    // Retrieve the original Kotlin KClass from the ObjCClass
    val kotlinCls: KClass<*>? = getOriginalKotlinClass(objcClass)

    // Print the fully‑qualified name of the original Kotlin class
    println("Original Kotlin class: ${kotlinCls?.qualifiedName}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/get-original-kotlin-class.html)

    