

# getValue

An extension operator that allows delegating a read-only property of type V to a property reference to a property of type V or its subtype.

```kotlin
inline operator fun <V> KProperty0<V>.getValue(thisRef: Any?, property: KProperty<*>): V(source)
```

import kotlin.reflect.KProperty

class Original(val msg: String)

class Wrapper(original: Original) {
    val message: String by original::msg
}

fun main() {
    val original = Original("Hello, Kotlin!")
    val wrapper = Wrapper(original)
    println(wrapper.message)  // Output: Hello, Kotlin!
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/get-value.html)

    