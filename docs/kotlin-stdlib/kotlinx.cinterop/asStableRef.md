

# asStableRef

Converts to StableRef this opaque pointer produced by StableRef.asCPointer.

```kotlin
inline fun <T : Any> CPointer<*>.asStableRef(): StableRef<T>(source)
```

```kotlin
import kotlinx.cinterop.*

class MyData(val message: String)

fun main() {
    // Create a Kotlin object and keep it alive on the native side
    val kotlinObject = MyData("Hello from Kotlin!")
    val stableRef = StableRef.create(kotlinObject)

    // Obtain the opaque C pointer that can be passed to native code
    val cPointer: CPointer<*> = stableRef.asCPointer()

    // ----- Simulate native side -----
    // The native side receives the CPointer and later converts it back
    val recoveredRef: StableRef<MyData> = cPointer.asStableRef()
    val recoveredObject: MyData = recoveredRef.get()
    // -------------------------------

    println(recoveredObject.message)   // prints: Hello from Kotlin!

    // Release the StableRef when done (prevents memory leak)
    recoveredRef.dispose()
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/as-stable-ref.html)

    