

# forEach

Performs the given action on each element.

```kotlin
inline fun <T> Array<out T>.forEach(action: (T) -> Unit)(source)
```

```kotlin
val fruits = arrayOf("Apple", "Banana", "Cherry")

fruits.forEach { fruit ->
    println("I love $fruit!")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/for-each.html)

    