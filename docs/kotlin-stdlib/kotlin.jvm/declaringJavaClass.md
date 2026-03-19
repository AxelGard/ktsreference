

# declaringJavaClass

Returns a Java Class instance of the enum the given constant belongs to.

```kotlin
val <E : Enum<E>> Enum<E>.declaringJavaClass: Class<E>(source)
```

```kotlin
enum class Color {
    RED, GREEN, BLUE
}

fun main() {
    val color: Color = Color.RED
    val javaClass: Class<Color> = color.declaringJavaClass

    println(javaClass)          // prints: class Color
    println(javaClass.name)     // prints: Color
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/declaring-java-class.html)

    