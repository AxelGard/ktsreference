

# setValue

An extension operator that allows delegating a mutable property of type V to a property reference to a mutable property of the same type V.

```kotlin
inline operator fun <V> KMutableProperty0<V>.setValue(thisRef: Any?, property: KProperty<*>, value: V)(source)
```

```kotlin
import kotlin.reflect.KMutableProperty0
import kotlin.reflect.KProperty

class Delegated<T>(private val backing: KMutableProperty0<T>) {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): T = backing.get()
    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: T) {
        backing.setValue(thisRef, property, value)   // uses the inline setValue operator
    }
}

var globalScore = 42

class Player {
    var score by Delegated(::globalScore)
}

fun main() {
    val p = Player()
    println(p.score)        // prints 42
    p.score = 100
    println(p.score)        // prints 100
    println(globalScore)    // prints 100
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/set-value.html)

    