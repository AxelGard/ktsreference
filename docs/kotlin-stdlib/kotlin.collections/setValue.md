

# setValue

Stores the value of the property for the given object in this mutable map.

```kotlin
inline operator fun <V> MutableMap<in String, in V>.setValue(thisRef: Any?, property: KProperty<*>, value: V)(source)
```

```kotlin
import kotlin.reflect.KProperty

val map = mutableMapOf<String, Any?>()

var userName: String by map
var userAge: Int by map

fun main() {
    userName = "John"
    userAge = 25

    println("Name: $userName, Age: $userAge")
    println("Map contents: $map")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/set-value.html)

    